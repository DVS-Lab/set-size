maindir = pwd;

mySnacks = dir('images/*.jpg');
snackNames = {};

for i = 1:length(mySnacks)
    [~,name,~] = fileparts(mySnacks(i).name);
    snackNames{end+1} = name;
end

% get participant output files
taskAFiles = dir('*_task_a_results.csv');
taskBFiles = dir('*_task_b_results.csv');

% open output files
fname = fullfile(maindir,'setsize_ratings_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'snackNames,preRatings_means,choosing_for_self_means,choosing_for_partner_means,\n');

sublist = [103 109 117];
preRatings = [];

% Get Ratings
for s = 1:length(sublist)
    % Get PreRatings
    subjectPreRatings = [];
    
    taskAFile = taskAFiles(s).name;
    fname = fullfile(maindir,taskAFile);
    fid = fopen(fname);
    taskAData = textscan(fopen(fname,'r'),'%s%d%d','Delimiter',',');
    fclose(fid);
    
    for i = 1:length(snackNames)
        snackRating = [];
        for j = 1:length(taskAData{1,1})
           [~,snackName,~] = fileparts(taskAData{1, 1}{j, 1});
           if isequal(snackNames{i},snackName)
              snackRating = [snackRating, taskAData{1, 2}(j)];
           end
        end
        subjectPreRatings = [subjectPreRatings,snackRating];
    end
    preRatings = [preRatings; subjectPreRatings];
    preRatings_means = [preRatings_means,preRatings];
    
    % Get PostRatings
    taskBFile = taskBFiles(s).name;
    fname = fullfile(maindir,taskBFile);
    fid = fopen(fname);
    taskBData = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
    fclose(fid);
    
    for i = 1:length(snackNames) % for each snack
        subjectData.Choices = [];
        for j = 1:length(subjectData.Choices) % for however many choices were made
            if snackNames == subjectData(j).Choices
                if subjectData(j)ChoosingFor == 1 % if participant was choosing for themselves
                    rating_You
            end
        end
    end
end
