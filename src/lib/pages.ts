/**
 * Hidden pages: built but unlaunched. Removed from the sitemap and given noindex.
 * While site.formationMode is true, every page is noindex anyway.
 */
export const hiddenPages: string[] = [
  '/council-members/',
  '/council/', // future-state member profiles (sample data)
  '/members/', // future-state member listing (sample data)
  '/supporters/', // future-state supporters (sample data)
];

export function isHiddenPath(pathname: string): boolean {
  return hiddenPages.some((p) => pathname === p || (p.endsWith('/') && pathname.startsWith(p)));
}
