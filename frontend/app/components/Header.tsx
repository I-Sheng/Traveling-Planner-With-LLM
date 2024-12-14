// components/Header.tsx
import Link from "next/link";
import React from "react";

const Header: React.FC = () => {
  return (
    <header className="p-4 bg-blue-500 text-white flex justify-between items-center">
      <h1 className="text-2xl font-bold">My Website</h1>
      <nav className="space-x-4">
          <Link href="/" className="hover:underline">isheng</Link>
          <Link href="/projects" className="hover:underline">Projects</Link>
          <Link href="/about" className="hover:underline">About</Link>
      </nav>
    </header>
  );
};

export default Header;

