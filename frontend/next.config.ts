import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // Set the output to 'export' for static file generation
  distDir: "out", // Custom output directory  //output: "standalone",
  env: {
    RECOMMEND_API_URL: process.env.RECOMMEND_API_URL || "http://recommend:5001",
    ROUTING_API_URL: process.env.ROUTING_API_URL || "http://routing:5002",
  },
};

export default nextConfig;
