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
          200: '#dbe3ef',
          700: '#243044',
          800: '#18212f',
          900: '#0d1420',
          950: '#090e16'
        },
        accent: {
          400: '#60a5fa',
          500: '#3b82f6',
          600: '#2563eb'
        },
        signal: {
          green: '#22c55e',
          amber: '#f59e0b',
          red: '#ef4444'
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
