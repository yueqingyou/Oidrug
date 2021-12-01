function main(rank1, rank2, w, alpha, beta, gamma, DorT, scenario, ~)
    clc
    clear

    if nargin < 8
        scenario = '1';
    end

    if nargin < 7
        DorT = '1';
    end

    if nargin < 6
        gamma = 0.01;
    end

    if nargin < 5
        beta = 0.01;
    end
    
    if nargin < 4
        alpha = 0.01;
    end

    if nargin < 3
        w = 0.3;
    end

    if nargin < 2
        rank2 = 90;
    end

    if nargin < 1
        rank1 = 70;
    end

load Disease-sim.mat disease_sim
load Drug-disease.mat didr
load Drug-sim1.mat drug_sim1
load Drug-sim2.mat drug_sim2
load Drug-target.mat drug_tar
load Target-sim.mat tar_sim
load SMat.mat smat

X = {};
Au = {};
Av = {};

if DorT == '2'
    X{2} = didr';
    X{1} = drug_tar;
    Au{2} = drug_sim1;
    Au{1} = drug_sim2;
    Av{2} = disease_sim;
    Av{1} = tar_sim;
    S = smat';
end

if DorT == '1'
    X{1} = didr';
    X{2} = drug_tar;
    Au{1} = drug_sim1;
    Au{2} = drug_sim2;
    Av{1} = disease_sim;
    Av{2} = tar_sim;
    S = smat';
end

yy = X{1};
nfolds = 10;
para = [alpha, beta, gamma];

[positiveId, crossval_id] = train_test_split(X{1}, nfolds, scenario);
% split the train and test

for fold = 1:nfolds
    X{1} = yy;
    PtestID  = positiveId(crossval_id==fold);

    % sample equal amount of negative sample
    negativeID = find(X{1}==0);
    num = numel(negativeID);
    Nidx = randperm(num);
    NtestID = negativeID(Nidx(1:length(PtestID)));

    X{1}(PtestID) = 0; % mask out the test data
    
    [U, V, ~] = Oidrug(X, w, Au, Av, S, rank1, rank2, para);
    
    predX = U{1} * V{1}';
    testScore = [yy(PtestID); yy(NtestID)];
    save('origin.mat', 'testScore')
    pred = [predX(PtestID); predX(NtestID)];
    save('pre.mat', "pred")
    fprintf('fold %d is ok', fold);

end
end
