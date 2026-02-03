/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./index.html",
        "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
        extend: {
            fontFamily: {
                'jp': ['"Noto Sans JP"', 'sans-serif'],
            },
            colors: {
                'sakura': '#fde2e6',
                'bamboo': '#d4e6c2',
                'indigo-jp': '#2b3a55',
            }
        },
    },
    plugins: [],
}
