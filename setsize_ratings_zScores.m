maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_ratings_zScores.csv');
fid_run = fopen(fname,'w'); % csv uses commas (,) & tsv uses tabs (\t)
fprintf(fid_run,'subj_id,zScore\n');

sublist = [102 109 110 113 115 117 118 119 120 121 122 123 124 125 126 127 128 131 132 135 136 137 138 139 140];
baseoutput = fullfile(maindir,'output');

% get participant output files
for s = sublist
    taskAFile = dir(fullfile(baseoutput,[num2str(s) '_task_a_results.csv']));
    myFiles = dir('*results.csv');
end

% get participant output files
for s = 1:length(myFiles)
    subj_id = sublist(s);
    file_name = myFiles(s).name;
    fname = fullfile(maindir,file_name);
    fid = fopen(fname);
    
    % defines what "C" (column) is from data output file
    C = textscan(fopen(fname,'r'),'%s%d%d','Delimiter',',','HeaderLines',1);
    fclose(fid);

    % get zScore
    zScore = zscore(taskAFile{2});
    
    % write in tmp_data
    tmp_data = [subj_id zScore];

    % write data to output file 'setsize_choice1rt_output.tsv'
    fprintf(fid_run,'%d,%s\n',tmp_data);
end
close(fid_run);
