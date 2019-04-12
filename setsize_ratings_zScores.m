maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_ratings_zScores.csv');
fid_run = fopen(fname,'w'); % csv uses commas (,) & tsv uses tabs (\t)
fprintf(fid_run,'subj_id,zScore\n');

sublist = [102 109 110 113 115 117 118 119 120 121 122 123 124 125 126 127 128 131 132 135 136 137 138 139 140];
subj_id = sublist(s);
baseoutput = fullfile(maindir,'output');

% get participant output files
for s = 1:length(sublist)-1
    taskAFile = dir(fullfile(baseoutput,[num2str(sublist(s)) '_task_a_results.csv']));
    
    % get participant output files
    fname = taskAFile(s).name;
    fid = fopen(fname);
    taskAData = textscan(fopen(fname,'r'),'%s%d%d','Delimiter',',');
    taskAData = cell2mat(taskAData(2));
    fclose(fid);
    
    % pull satisfaction ratings
    ratings = double(taskAData);
    
    % get zScore
    zScore = zscore(ratings);
    zScore = mean(zScore);
    
    % write in tmp_data
    tmp_data = [subj_id zScore];

    % write data to output file 'setsize_choice1rt_output.tsv'
    fprintf(fid_run,'%d,%s\n',tmp_data);

end
fclose(fid_run);
