// Dependency-free static export for Vercel, served from the domain root.
import { copyFileSync, mkdirSync, readFileSync, readdirSync, rmSync, writeFileSync } from 'node:fs';
import { dirname, extname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const output = join(root, 'dist');
const pages = ['index.html', 'moja-droga.html', 'twoja-droga.html', 'coaching.html',
  'interwencja-kryzysowa.html', 'prism-brain-mapping.html', 'mtq-plus.html',
  'terapia-dzwiekiem.html', 'warsztaty-i-szkolenia.html'];
const assetTypes = new Set(['.webp', '.jpg', '.jpeg', '.png', '.svg', '.woff', '.woff2']);

rmSync(output, { recursive: true, force: true });
mkdirSync(output, { recursive: true });
function copy(relative) {
  const target = join(output, relative);
  mkdirSync(dirname(target), { recursive: true });
  copyFileSync(join(root, relative), target);
}
function assets(relative) {
  for (const entry of readdirSync(join(root, relative), { withFileTypes: true })) {
    const file = join(relative, entry.name);
    if (entry.isDirectory()) assets(file);
    else if (entry.isFile() && (assetTypes.has(extname(file)) || entry.name.endsWith('-OFL.txt'))) copy(file);
  }
}
for (const file of [...pages, 'styles.css', 'script.js']) copy(file);
assets('assets');
// Pages retains its subdirectory URLs; the Vercel artifact uses the domain root,
// including when a visitor opens an unknown, deeply nested URL.
const notFound = readFileSync(join(root, '404.html'), 'utf8')
  .replace(/<!--[^]*?-->/g, '')
  .replaceAll('/Katarzyna_chalas_page/', '/');
writeFileSync(join(output, '404.html'), notFound);
console.log(`Exported ${pages.length} pages, 404, CSS, JS and public assets to dist/`);
