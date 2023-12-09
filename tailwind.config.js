/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      fontSize: {
        huge: '8rem'
      },
      colors: {
        primary: "#0284C7",
        'dark-primary': "#172554",
        'light-primary': "#A5F3FC",
        accent: "#EAB308",
        background: "#F5F5F5",
        text: "#0F172A",
        'secondary-text': "#4B5563"
      }
    },
  },
  plugins: [],
}