// pages/projects.tsx
import React from "react";
import Header from "@/app/components/Header";
import Footer from "@/app/components/Footer";

const ProjectsPage: React.FC = () => {
  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow flex items-center justify-center bg-gradient-to-b from-purple-50 to-purple-100">
        <div className="text-center p-4">
          <h2 className="text-3xl font-bold mb-4">My Projects</h2>
          <p className="text-lg text-gray-700 max-w-lg">
            Check out some of my recent projects in software development, web
            design, and more.
          </p>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export default ProjectsPage;
