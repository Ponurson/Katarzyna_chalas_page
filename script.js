(() => {
  const header = document.querySelector('[data-header]');
  const toggle = document.querySelector('[data-menu-toggle]');
  const navigation = document.querySelector('[data-navigation]');
  if (!header || !toggle || !navigation) return;
  document.documentElement.classList.add('js');
  const desktop = window.matchMedia('(min-width: 1081px)');
  const isOpen = () => toggle.getAttribute('aria-expanded') === 'true';
  const closeMenu = (returnFocus = false) => {
    navigation.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Otwórz menu');
    document.body.classList.remove('menu-open');
    if (returnFocus) toggle.focus();
  };
  toggle.addEventListener('click', () => {
    if (isOpen()) return closeMenu();
    navigation.classList.add('is-open');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Zamknij menu');
    document.body.classList.add('menu-open');
  });
  navigation.addEventListener('click', (event) => {
    if (event.target.closest('a')) closeMenu();
  });
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && isOpen()) closeMenu(true);
  });
  document.addEventListener('click', (event) => {
    if (isOpen() && !header.contains(event.target)) closeMenu();
  });
  document.addEventListener('focusin', (event) => {
    if (isOpen() && !header.contains(event.target)) closeMenu();
  });
  desktop.addEventListener('change', () => closeMenu());
  const updateHeader = () => header.classList.toggle('has-shadow', window.scrollY > 8);
  updateHeader();
  window.addEventListener('scroll', updateHeader, { passive: true });
})();
