// /pages/api/recommend.ts
import type { NextApiRequest, NextApiResponse } from "next";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  if (req.method !== "POST") {
    return res.status(405).json({ error: "Method not allowed" });
  }

  const { day, preference } = req.body;
  console.log("Calling recommend API");
  try {
    // Make a request to the local API (or external endpoint) with the data
    const apiUrl = process.env.NEXT_PUBLIC_RECOMMEND_API_URL;
    const response = await fetch(`${apiUrl}/recommend`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ day, preference }),
    });

    if (!response.ok) {
      return res
        .status(response.status)
        .json({ error: "Failed to fetch recommended sites" });
    }

    const data = await response.json();
    return res.status(200).json(data);
  } catch (error) {
    console.error("Error fetching recommended sites:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
}
