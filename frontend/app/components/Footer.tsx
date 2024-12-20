import React from "react";

const Footer: React.FC = () => {
  return (
    <footer className="bg-white shadow-md py-4 px-8 mt-8">
      <div className="flex flex-col items-center text-sm text-gray-600">
        {/* Author Name */}
        <div className="font-semibold">Author: Isheng, Lee</div>

        {/* Email */}
        <div className="text-gray-500">
          Email:
          <a
            href="mailto:110703011@g.nccu.edu.tw"
            className="text-blue-600 hover:underline ml-1"
          >
            110703011@g.nccu.edu.tw
          </a>
        </div>

        {/* Additional Style */}
        <div className="mt-2 text-xs text-gray-400">
          © {new Date().getFullYear()} ITravel. All Rights Reserved.
        </div>
      </div>
    </footer>
  );
};

export default Footer;
