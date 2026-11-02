import { getCollection } from 'astro:content';

/** All Council members, sorted alphabetically by surname then first name. */
export async function getMembersBySurname() {
  const all = await getCollection('members');
  return all.sort((a, b) =>
    a.data.surname.localeCompare(b.data.surname, 'en-AU') || a.data.firstName.localeCompare(b.data.firstName, 'en-AU'));
}
