import type { Metadata } from "next";
import localFont from "next/font/local";
import "@/app/globals.css";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "嘉義旅遊規劃系統",
  description: "幫助使用者規劃嘉義一日遊",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-tw">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-blue-100 text-black`}
      >
        {children}
      </body>
    </html>
  );
}
