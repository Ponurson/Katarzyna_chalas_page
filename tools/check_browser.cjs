/* Sequential acceptance checks and screenshots; starts a loopback-only preview.
 * npm ci && npm run check:browser
 * CHROMIUM_PATH may point to an installed Chromium (automatically used on Pi).
 */
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const { spawn, execFileSync } = require('node:child_process');
const { chromium } = require('playwright');
const AxeBuilder = require('@axe-core/playwright').default;

const root = path.resolve(__dirname, '..');
const output = path.join(root, 'artifacts/browser');
const pages = ['index.html', 'moja-droga.html', 'twoja-droga.html', 'coaching.html',
  'interwencja-kryzysowa.html', 'prism-brain-mapping.html', 'mtq-plus.html',
  'terapia-dzwiekiem.html', 'warsztaty-i-szkolenia.html'];
const sizes = [[320, 812], [375, 812], [390, 844], [768, 1024], [1440, 900]];
const report = { date: new Date().toISOString(), views: [], journeys: [], errors: [], temperatures: [] };

function checkPi() {
  const temperature = '/sys/class/thermal/thermal_zone0/temp';
  if (!fs.existsSync('/proc/device-tree/model') ||
      !fs.readFileSync('/proc/device-tree/model', 'utf8').includes('Raspberry Pi')) return;
  const value = Number(fs.readFileSync(temperature, 'utf8').trim());
  assert(Number.isFinite(value) && value > 0 && value < 72000, `Pi: temperatura ${value} m°C`);
  const status = execFileSync('vcgencmd', ['get_throttled'], { encoding: 'utf8' }).trim();
  const match = status.match(/^throttled=0x([0-9a-f]+)$/i);
  assert(match && (parseInt(match[1], 16) & 0xf) === 0, `Pi: ${status}`);
  report.temperatures.push(value);
}

function startPreview() {
  const child = spawn(process.env.PYTHON || 'python3', ['tools/serve_demo.py', '--port', '0'], { cwd: root });
  const ready = new Promise((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error('Nie uruchomiono lokalnego podglądu.')), 10000);
    child.once('error', error => { clearTimeout(timer); reject(error); });
    child.once('exit', code => { clearTimeout(timer); reject(new Error(`Podgląd zakończony: ${code}`)); });
    child.stdout.on('data', data => {
      const match = data.toString().match(/http:\/\/127\.0\.0\.1:\d+/);
      if (match) { clearTimeout(timer); resolve(match[0]); }
    });
    child.stderr.on('data', data => process.stderr.write(data));
  });
  return { child, ready };
}

async function settle(page) {
  await page.evaluate(async () => {
    await document.fonts.ready;
    // Load images below the fold before checking resources and full-page captures.
    await Promise.all([...document.images].map(async image => {
      image.loading = 'eager';
      await image.decode();
    }));
    window.scrollTo({ top: 0, behavior: 'instant' });
  });
}

async function menuChecks(page) {
  const toggle = page.locator('[data-menu-toggle]');
  const nav = page.locator('[data-navigation]');
  const state = async open => {
    assert.equal(await toggle.getAttribute('aria-expanded'), String(open));
    assert.equal(await toggle.getAttribute('aria-label'), open ? 'Zamknij menu' : 'Otwórz menu');
    assert.equal(await nav.isVisible(), open);
  };
  await state(false);
  await toggle.focus();
  await page.keyboard.press('Enter');
  await state(true);
  await page.keyboard.press('Escape');
  await state(false);
  assert(await toggle.evaluate(element => element === document.activeElement));
  await page.keyboard.press('Space');
  await state(true);
  await page.mouse.click(5, 500);
  await state(false);
  await toggle.click();
  await page.locator('main').focus();
  await state(false);
  await toggle.click();
  await nav.locator('a').first().click();
  await state(false);
  assert(!await page.locator('body').evaluate(body => body.classList.contains('menu-open')));
}

async function layout(page) {
  return page.evaluate(() => {
    const box = selector => {
      const element = document.querySelector(selector);
      if (!element) return null;
      const rect = element.getBoundingClientRect();
      return { width: rect.width, height: rect.height };
    };
    const images = [...document.images].map(image => ({ src: image.currentSrc.split('/').pop(),
      loaded: image.complete && image.naturalWidth > 0,
      width: image.getBoundingClientRect().width, height: image.getBoundingClientRect().height,
      naturalWidth: image.naturalWidth, naturalHeight: image.naturalHeight,
      fit: getComputedStyle(image).objectFit }));
    const buttons = [...document.querySelectorAll('.button')].map(button => button.getBoundingClientRect())
      .filter(rect => rect.width > 0 && rect.height > 0);
    const overlaps = buttons.some((a, i) => buttons.slice(i + 1).some(b =>
      Math.min(a.right, b.right) - Math.max(a.left, b.left) > 1 &&
      Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) > 1));
    return { documentWidth: document.documentElement.scrollWidth, viewport: innerWidth,
      images, overlaps, about: box('.about-portrait img'), aboutText: box('.about-copy'),
      contact: box('.contact-image img'), contactBlock: box('.contact-image'),
      h1Font: getComputedStyle(document.querySelector('h1')).fontFamily,
      bodyFont: getComputedStyle(document.body).fontFamily,
      fonts: [...document.fonts].map(font => ({ family: font.family, style: font.style, status: font.status })) };
  });
}

(async () => {
  fs.mkdirSync(output, { recursive: true });
  checkPi();
  if (fs.existsSync('/usr/bin/vcgencmd')) {
    const recent = execFileSync('dmesg', ['--since', '10 minutes ago'], { encoding: 'utf8' });
    assert(!/Undervoltage detected!/i.test(recent), 'Pi: niedawny spadek napięcia — kontrola wstrzymana.');
  }
  const preview = startPreview();
  let browser;
  try {
    const base = await preview.ready;
    const executablePath = process.env.CHROMIUM_PATH || (fs.existsSync('/usr/bin/chromium') ? '/usr/bin/chromium' : undefined);
    browser = await chromium.launch({ executablePath, headless: true });
    report.browser = browser.version();
    for (const [width, height] of sizes) {
      const context = await browser.newContext({ viewport: { width, height }, reducedMotion: 'reduce', locale: 'pl-PL' });
      const page = await context.newPage();
      page.on('pageerror', error => report.errors.push(error.message));
      page.on('console', message => { if (message.type() === 'error') report.errors.push(message.text()); });
      page.on('requestfailed', request => report.errors.push(`${request.url()}: ${request.failure()?.errorText}`));
      page.on('response', response => { if (response.status() >= 400) report.errors.push(`${response.status()} ${response.url()}`); });
      for (const file of pages) {
        checkPi();
        assert.equal((await page.goto(`${base}/${file}`)).status(), 200, file);
        await settle(page);
        const geometry = await layout(page);
        assert(geometry.documentWidth <= width, `${file} ${width}: poziome przewijanie`);
        assert(!geometry.overlaps, `${file} ${width}: nakładające się CTA`);
        assert(geometry.images.every(image => image.loaded), `${file}: obraz niedostępny`);
        assert(geometry.h1Font.startsWith('"Allrounder Antiqua Test"'));
        assert(geometry.bodyFont.startsWith('Montserrat'));
        assert(geometry.fonts.filter(font => font.style === 'normal').every(font => font.status === 'loaded'));
        for (const image of geometry.images) {
          if (image.fit === 'fill') assert(Math.abs(image.width / image.height - image.naturalWidth / image.naturalHeight) < .005, `${file}: zdeformowany obraz`);
        }
        if (geometry.about && width > 1080) {
          const image = geometry.images.find(image => image.src.startsWith('about-'));
          const paintedHeight = Math.min(image.height, image.width * image.naturalHeight / image.naturalWidth);
          const ratio = paintedHeight / geometry.aboutText.height;
          assert(ratio >= .7 && ratio <= 1.01, `O mnie: wysokość zdjęcia / tekstu ${ratio}`);
          geometry.aboutHeightRatio = ratio;
        }
        const result = await new AxeBuilder({ page }).withTags(['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa']).analyze();
        const violations = result.violations.map(item => ({ id: item.id, impact: item.impact, targets: item.nodes.map(node => node.target) }));
        const screenshot = `${file.replace('.html', '')}-${width}x${height}.jpg`;
        await page.screenshot({ path: path.join(output, screenshot), fullPage: true, type: 'jpeg', quality: 78 });
        if (file === 'index.html') {
          await page.screenshot({ path: path.join(output, `hero-${width}.jpg`), type: 'jpeg', quality: 85 });
          for (const [section, selector] of [['kontakt', '#kontakt'], ['cennik', '.pricing'], ['oferta', '#oferta'], ['omnie', '#omnie']]) {
            await page.locator(selector).evaluate(element => scrollTo({ top: scrollY + element.getBoundingClientRect().top - 112, behavior: 'instant' }));
            await page.screenshot({ path: path.join(output, `${section}-${width}.jpg`), type: 'jpeg', quality: 82 });
          }
          await page.evaluate(() => scrollTo({ top: 0, behavior: 'instant' }));
        }
        report.views.push({ file, width, height, screenshot, ...geometry, violations,
          axeIncomplete: result.incomplete.map(item => item.id) });
        assert.deepEqual(violations, [], `${file} ${width}: axe`);
        await page.keyboard.press('Tab');
        assert(await page.locator('.skip-link').evaluate(link => link === document.activeElement), `${file}: pierwszy Tab`);
        assert(await page.locator('.skip-link').evaluate(link => getComputedStyle(link).outlineStyle !== 'none'));
        await page.keyboard.press('Enter');
        assert.equal(await page.evaluate(() => document.activeElement.id), 'main-content', `${file}: skip-link`);
        assert.equal(await page.evaluate(() => getComputedStyle(document.documentElement).scrollBehavior), 'auto');
        if (width === 390) await menuChecks(page);
        console.log(`OK ${file} ${width}×${height}: zasoby, układ, klawiatura, axe, zrzut`);
      }
      await context.close();
    }
    // Exercise each complete home → detail → contact journey, plus the brand and menus.
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, reducedMotion: 'reduce' });
    const page = await context.newPage();
    for (const file of pages.slice(1)) {
      await page.goto(`${base}/index.html`);
      await page.locator(`.journey a[href="${file}"], .offer a[href="${file}"]`).click();
      assert.equal(new URL(page.url()).pathname, `/${file}`);
      await page.locator('.article-cta a').click();
      assert.equal(new URL(page.url()).pathname + new URL(page.url()).hash, '/index.html#kontakt');
      await page.waitForFunction(() => Math.abs(document.querySelector('#kontakt').getBoundingClientRect().top - 112) < 2);
      report.journeys.push(file);
    }
    await page.goto(`${base}/coaching.html`);
    await page.locator('header .brand').click();
    assert.equal(new URL(page.url()).pathname, '/index.html');
    for (const selector of ['.site-nav', '.footer-nav']) {
      await page.goto(`${base}/coaching.html`);
      await page.locator(`${selector} a[href="index.html#oferta"]`).click();
      assert.equal(new URL(page.url()).hash, '#oferta');
    }
    // A popup opens the exact existing LinkedIn URL. Block the external navigation
    // locally: this checks the contract without depending on LinkedIn anti-bot rules.
    for (const label of ['Umów konsultację', 'Napisz wiadomość']) {
      await page.goto(`${base}/index.html#kontakt`);
      let destination;
      await context.route('https://www.linkedin.com/**', route => {
        destination = route.request().url();
        return route.fulfill({ status: 200, contentType: 'text/html', body: '<title>CTA test</title>' });
      });
      const popupEvent = context.waitForEvent('page');
      await page.locator('#kontakt').getByRole('link', { name: label, exact: true }).click();
      const popup = await popupEvent;
      await popup.waitForLoadState();
      assert.equal(destination, 'https://www.linkedin.com/in/katarzyna-cha%C5%82as-747831b8/');
      assert.equal(await popup.evaluate(() => window.opener), null);
      await popup.close();
      await context.unroute('https://www.linkedin.com/**');
    }
    // The preview must not expose the source documents, repository or workbook.
    for (const resource of ['/Wytyczne/Brief%20stronka.pdf', '/.git/config', '/teksty-strony.xlsx', '/tools/make_content_template.py']) {
      assert.equal((await context.request.get(base + resource)).status(), 404, resource);
    }
    await page.setViewportSize({ width: 390, height: 844 });
    await page.goto(`${base}/index.html`);
    await page.locator('[data-menu-toggle]').click();
    await page.setViewportSize({ width: 1440, height: 900 });
    await page.waitForFunction(() => document.querySelector('[data-menu-toggle]').getAttribute('aria-expanded') === 'false');
    await page.setViewportSize({ width: 390, height: 844 });
    assert(!await page.locator('[data-navigation]').isVisible());
    await context.close();
    const noScript = await browser.newContext({ javaScriptEnabled: false, viewport: { width: 390, height: 844 } });
    const plain = await noScript.newPage();
    await plain.goto(`${base}/index.html`);
    assert(await plain.locator('.site-nav a').first().isVisible());
    await plain.locator('.site-nav a[href="#oferta"]').click();
    assert.equal(new URL(plain.url()).hash, '#oferta');
    await noScript.close();
    assert.deepEqual(report.errors, [], 'Błędy JavaScript / sieci');
    report.status = 'passed';
    console.log(`OK — ${report.views.length} widoków, 8 pełnych ścieżek, menu, CTA, reduced-motion, brak JS i prywatne materiały. Raport: artifacts/browser/report.json`);
  } catch (error) {
    report.status = 'failed';
    report.failure = error.stack;
    throw error;
  } finally {
    if (browser) await browser.close();
    preview.child.kill();
    fs.writeFileSync(path.join(output, 'report.json'), JSON.stringify(report, null, 2) + '\n');
  }
})().catch(error => { console.error(error); process.exitCode = 1; });
