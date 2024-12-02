// pages/about.tsx
import React from "react";
import Header from "@/app/components/Header";
import Footer from "@/app/components/Footer";

const AboutPage: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow flex items-center justify-center bg-gradient-to-b from-green-50 to-green-100">
        <div className="text-center p-4">
          <h2 className="text-3xl font-bold mb-4">About Me</h2>
          <p className="text-lg text-gray-700 max-w-lg">
            Hello! I’m a computer science student deeply interested in software
            development, particularly in web technologies, artificial
            intelligence, and information security.
          </p>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default AboutPage;
