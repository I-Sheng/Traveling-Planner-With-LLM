import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  // Set the output to 'export' for static file generation
  distDir: "out", // Custom output directory
  //output: "standalone",
  env: {
    NEXT_PUBLIC_RECOMMEND_API_URL:
      process.env.RECOMMEND_API_URL || "http://localhost:5001",
    NEXT_PUBLIC_ROUTING_API_URL:
      process.env.ROUTING_API_URL || "http://localhost:5002",
  },
};

export default nextConfig;
