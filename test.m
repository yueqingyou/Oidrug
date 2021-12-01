FileData = load('origin.mat');
writematrix('origin.csv', FileData.testScore);

FileData = load('pre.mat');
writematrix('pre.csv', FileData.pred);
