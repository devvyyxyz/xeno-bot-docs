document.addEventListener('DOMContentLoaded', function () {
  try {
    // Find any nav links that point to the tags pages
    const tagLinks = Array.from(document.querySelectorAll('.md-nav__list a[href*="/tags/"]'));
    if (!tagLinks.length) return;
    // For each tag link, find the top-level nav group (closest li which contains the nav)
    tagLinks.forEach(a => {
      const groupNav = a.closest('nav[data-md-level]');
      if (!groupNav) return;
      const groupLi = groupNav.closest('li.md-nav__item');
      if (!groupLi) return;
      // Remove the whole group from the DOM
      groupLi.remove();
    });
  } catch (e) {
    // swallow errors; this script only enhances the nav
    console.warn('hide-tags-nav failed', e);
  }
});
