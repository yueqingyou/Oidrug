FileData = load('origin.mat');
writematrix(FileData.testScore, 'origin.csv');

FileData = load('pre.mat');
writematrix(FileData.pred, 'pre.csv');
