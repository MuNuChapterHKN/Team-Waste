module.exports = {
  // purge: ['./src/**/*.svelte'],
  content: ['./src/**/*.svelte'],
  // darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [
    require('daisyui')
  ],
}
