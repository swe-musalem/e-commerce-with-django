const colors = require('tailwindcss/colors')


module.exports = {
  content: ["./myapp/templates/**/.{html,js}"],
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        amber: colors.amber,
        emerald: colors.emerald,
        slate:colors.slate,
    }},
  },
  variants: {
    extend: {
    },
  },
  plugins: [],
}
