import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // Set the output to 'export' for static file generation
  output: "export",
  //output: "standalone",
  // Enable React Strict Mode for highlighting potential issues in development
  // reactStrictMode: true,
};

export default nextConfig;
