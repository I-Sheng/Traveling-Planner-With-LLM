var fs = require('fs');
var path = require('path');
// Directory containing images
var imagesDir = path.join(__dirname, 'images');
// Function to replace spaces in filenames with underscores
var renameImages = function (directory) {
    try {
        var files = fs.readdirSync(directory);
        files.forEach(function (file) {
            var oldPath = path.join(directory, file);
            if (fs.statSync(oldPath).isFile() && /\s/.test(file)) {
                var newFileName = file.replace(/\s/g, '_');
                var newPath = path.join(directory, newFileName);
                fs.renameSync(oldPath, newPath);
                console.log("Renamed: ".concat(file, " -> ").concat(newFileName));
            }
        });
        console.log('All files have been renamed successfully.');
    }
    catch (error) {
        console.error('Error renaming files:', error);
    }
};
// Call the function
renameImages(imagesDir);
