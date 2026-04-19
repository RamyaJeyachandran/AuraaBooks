/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        accent: 'var(--accent)',
        accent2: 'var(--accent2)',
        'accent-light': 'var(--accent-light)',
        'accent-text': 'var(--accent-text)',
      },
      borderRadius: {
        'lg': 'var(--radius)',
      }
    },
  },
  plugins: [],
}
