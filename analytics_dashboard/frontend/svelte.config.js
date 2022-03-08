import adapter from "@sveltejs/adapter-static";
import preprocess from "svelte-preprocess";

/** @type {import('@sveltejs/kit').Config} */
const config = {
  // Consult https://github.com/sveltejs/svelte-preprocess
  // for more information about preprocessors
  preprocess: preprocess(),

  kit: {
    adapter: adapter(),
    prerender: {
      default: true,
    },

    // hydrate the <div id="svelte"> element in src/app.html
    // target: '#svelte',
    // ssr: false // This is deprecated and could be a problem

    vite: {
      ssr: {
        noExternal: ["chart.js", "@cubejs-client/core"],
      },
    },
  },
};

export default config;
