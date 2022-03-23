// This file is just used to disable ssr, needed when running the website in dev mode
// Disabling ssr is needed because of chart js and cube js, and because the final website won't use ssr
/** @type {import('@sveltejs/kit').Handle} */
export async function handle({ event, resolve }) {
  const response = await resolve(event, {
    ssr: false
  });

  return response;
}