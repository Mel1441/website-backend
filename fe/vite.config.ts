import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "src"),
      "@components": path.resolve(__dirname, "src/components"),
      "@pages": path.resolve(__dirname, "src/pages"),
      "@services": path.resolve(__dirname, "src/services"),
    },
  },
  server: {
    port: 5173,
    open: true,
  },
});
// vite.config.js
//import { defineConfig } from 'vite';
//import react from '@vitejs/plugin-react';
//import tailwindcss from '@tailwindcss/vite';

//export default defineConfig({
  //plugins: [react()],
  //root: '.', // your project root
  //tailwindcss()
//});