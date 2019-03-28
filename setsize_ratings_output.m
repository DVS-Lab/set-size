maindir = pwd;

mySnacks = dir('images/*.jpg');
snackNames = {};

for i = 1:length(mySnacks)
    [~,name,~] = fileparts(mySnacks(i).name);
    snackNames{end+1} = name;
end

% list subject ID's
sublist = [103 109 117];
baseoutput = fullfile(maindir,'output');

% get participant output files
for s = sublist
taskAFiles = dir(fullfile(baseoutput,[num2str(s) '*_task_a_results.csv']));
taskBFiles = dir('*_task_b_results.csv');
end

% open output files
fname = fullfile(maindir,'setsize_ratings_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'snackNames,preRatings_means,rating_You_means,rating_Partner_means,\n');

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
        rating_You = [];
        rating_Partner = [];
        for j = 1:length(subjectData.Choices) % for however many choices were made
            if snackNames == subjectData.Choices % place choices in temporary bracket
                if subjectData(j)ChoosingFor == 1 % if participant was choosing for themselves
                    rating_You.append(subjectData.Choices);
                    rating_You = str2double(C{10},(j));
                else % if participant was choosing for partner
                    rating_Partner.append(subjectData.Choices);
                    rating_Partner = str2double(C{10},(j));
                end
            end
        end
    end
    rating_You_means = [rating_You_means,rating_You];
    rating_Partner_means = [rating_Partner_means,rating_Partner];
    
    % write in tmp_data
    tmp_data = [snackNames preRatings_means rating_You_means rating_Partner_means];

    % write data to output file 'setsize_ratings_output.tsv'
    fprintf(fid_run,'%s,%s,%s,%s\n',tmp_data);
end

fclose(fid_run);
