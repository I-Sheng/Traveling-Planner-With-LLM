// /pages/api/recommend.ts
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { day, sites } = req.body;

  try {
    // Make a request to the local API (or external endpoint) with the data
    const response = await fetch("http://localhost:5002/routing", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ day, sites }),
    });

    if (!response.ok) {
      return res
        .status(response.status)
        .json({ error: "Failed to fetch recommended sites" });
    }

    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    return res.status(500).json({ error: "Internal Server Error" });
  }
}
