maindir = pwd;

mySnacks = dir('images/*.jpg');
snackNames = {};

for i = 1:length(mySnacks)
    [~,name,~] = fileparts(mySnacks(i).name);
    snackNames{end+1} = name;
end

% list subject ID's
sublist = [102 109 117];
baseoutput = fullfile(maindir,'output');

% open output files
fname = fullfile(maindir,'setsize_ratings_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'snackNames,preRatings_means,you_means,partner_means\n');

% set up empty brackets
preRatings_means = [];
you_means = [];
partner_means = [];

% get participant output files
for s = sublist
    taskAFile = dir(fullfile(baseoutput,[num2str(s) '_task_a_results.csv']));
    taskBFile = dir(fullfile(baseoutput,['subject_' num2str(s) '_partner*_task_b_results.csv']));
    
% get PreRatings
    subjectPreRatings = [];
    subjectYouRatings = [];
    subjectPartnerRatings = [];

    fname = taskAFile.name;
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
        subjectPreRatings = [subjectPreRatings,mean(snackRating)];
    end
    preRatings_means = [preRatings_means,subjectPreRatings];
    
    % get PostRatings
    fname = taskBFile.name;
    fid = fopen(fname);
    taskBData = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
    fclose(fid);
    
    for i = 1:length(snackNames)
        rating_You = [];
        rating_Partner = [];
        for j = 1:length(taskBData{1,1})
           [~,snackName,~] = fileparts(taskBData{1, 7}{j, 1});
           if isequal(snackNames{i},snackName)
              if taskBData{1,13}{j,1} == '1'
                rating_You = [rating_You, str2num(taskBData{1, 10}{j, 1})];
              else
                rating_Partner = [rating_Partner, str2num(taskBData{1, 10}{j, 1})];
              end 
           end
        end
        subjectYouRatings = [subjectYouRatings,mean(rating_You)];
        subjectPartnerRatings = [subjectPartnerRatings,mean(rating_Partner)];
    end
    you_means = [you_means,subjectYouRatings];
    partner_means = [partner_means,subjectPartnerRatings];
end

% write in tmp_data
tmp_data = [snackNames preRatings_means you_means partner_means];

% write data to output file 'setsize_ratings_output.tsv'
fprintf(fid_run,'%s,%s,%s,%s\n',tmp_data{:});

fclose(fid_run);
