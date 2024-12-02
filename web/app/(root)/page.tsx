// pages/index.tsx
import React from "react";
import Header from "@/app/components/Header";
import MainContent from "@/app/components/MainContent";
import Footer from "@/app/components/Footer";

const HomePage: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow bg-gradient-to-b from-blue-50 to-blue-100">
        <MainContent />
      </main>
      <Footer />
    </div>
  );
};

export default HomePage;
