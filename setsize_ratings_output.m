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
fname = fullfile(maindir,'setsize_ratings_output10.csv');
fid_run = fopen(fname,'w'); % csv uses commas (,) & tsv uses tabs (\t)
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
           [~,snackName,~] = fileparts(taskAData{1}{j});
           if isequal(snackNames{i},snackName)
              snackRating = [snackRating, taskAData{2}(j)];
           end
        end
        subjectPreRatings = [subjectPreRatings,snackRating];
    end
    preRatings_means = [preRatings_means;subjectPreRatings];
    
    % get PostRatings
    fname = taskBFile.name;
    fid = fopen(fname);
    taskBData = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
    fclose(fid);
    
    for i = 1:length(snackNames) % for all snack names
        rating_You = [];
        rating_Partner = [];
        for j = 1:length(taskBData{1,1})
           [~,snackName,~] = fileparts(taskBData{1, 7}{j, 1});
           if isequal(snackNames{i},snackName)
               if isequal(taskBData{12}{j},'0') % non-computer responses
                  if taskBData{13}{j} == '1' % rating for yourself
                    rating_You = [rating_You, str2num(taskBData{10}{j})];
                  else % rating for your partner
                    rating_Partner = [rating_Partner, str2num(taskBData{10}{j})];
                  end
               end
           end
        end
        subjectYouRatings = [subjectYouRatings,nanmean(rating_You)];
        subjectPartnerRatings = [subjectPartnerRatings,nanmean(rating_Partner)];
    end
    you_means = [you_means;subjectYouRatings];
    partner_means = [partner_means;subjectPartnerRatings];
end

% format data
snackNames = snackNames(1:end-1)';
you_means = you_means(:,1:end-1);
partner_means = partner_means(:,1:end-1);

% get means across all subjects
preRatings_means = nanmean(preRatings_means)';
you_means = nanmean(you_means)';
partner_means = nanmean(partner_means)';

% write in tmp_data
tmp_data = [snackNames, num2cell(preRatings_means), num2cell(you_means), num2cell(partner_means)];

% cell2csv('testoutput.csv',tmp_data);

% write data to output file 'setsize_ratings_output.tsv'
fprintf(fid_run,'%s,%f,%f,%f\n',tmp_data{:});

fclose(fid_run);
