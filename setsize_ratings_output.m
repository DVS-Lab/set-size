clear;
maindir = pwd;

% Get participant output files
myFiles = dir('*results.csv');

% open output files
fname = fullfile(maindir,'setsize_h2_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id,partner_choice_means,\n');

sublist = [103 109 117];

for s = 1:length(myFiles)   
    subj_id = sublist(s);
    file_name = myFiles(s).name;
    fname = fullfile(maindir,file_name);
    fid = fopen(fname);
    
    % defines what "C" (column) is from data output file
    C = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
    fclose(fid);

    trial_data = '';
    
    % define partner_choice_means
    partner_choice_means = [];
    
    % H2A: find partner_choice_means
    for i = 1:length(C{12})
        if isequal(C{12}(i),{'0'}) % non-computer responses
            if isequal(C{13}(i),{'2'}) % choosing for partner
                partner_choice = str2double(C{10}(i));
                partner_choice_means = [partner_choice_means,partner_choice];
            end
        end
        %H2B: attach to this statement?
        
    
    % somehow compare intial ratings and post-ratings
