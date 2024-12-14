// components/MainContent.tsx
import React from "react";

const MainContent: React.FC = () => {
  return (
    <section className="flex flex-col items-center justify-center py-16 text-center">
      <h2 className="text-3xl font-bold mb-4">Welcome to My Site</h2>
      <p className="text-lg text-gray-700 max-w-xl">
        I&apos;m a computer science student based in Taipei, Taiwan, with a
        strong passion for technology, programming, and innovation. Alongside
        pursuing my degree, I&apos;m deeply interested in exploring the fields
        of cybersecurity and software development.
      </p>
    </section>
  );
};

export default MainContent;
