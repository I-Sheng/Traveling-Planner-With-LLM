import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // Set the output to 'export' for static file generation
  distDir: "out", // Custom output directory  //output: "standalone",
  // Enable React Strict Mode for highlighting potential issues in development
  // reactStrictMode: true,
};

export default nextConfig;
