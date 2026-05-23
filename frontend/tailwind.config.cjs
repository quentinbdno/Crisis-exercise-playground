/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        surface: {
          50: '#f8fafc',
          100: '#eef2f7',
          800: '#18212f',
          900: '#0d1420',
          950: '#080d14'
        },
        accent: {
          500: '#2f80ed',
          600: '#1f6fd2'
        },
        signal: {
          green: '#2fb344',
          amber: '#f59f00',
          red: '#e03131'
        }
      },
      boxShadow: {
        panel: '0 1px 0 rgba(148, 163, 184, 0.18)'
      }
    }
  },
  plugins: [
    function ({ addVariant }) {
      addVariant('light', ':root.light &');
    }
  ]
};
