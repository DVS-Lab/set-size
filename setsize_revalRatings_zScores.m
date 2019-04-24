%% note that we are excluding monetary selections for these analyses

clear;
maindir = pwd;

% Get task B data
taskBFile = dir('*_task_b_results_z_scores_tt.csv'); % make sure these files are in the main directory. I'll fix this later, but for now we're just putting that stuff here.

% open output files
fname = fullfile(maindir,'setsize_revalRatings_zScores_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id,you_high2_rev,you_high3_rev,you_high6_rev,you_high12_rev,you_mixed2_rev,you_mixed3_rev,you_mixed6_rev,you_mixed12_rev,partner_high2_rev,partner_high3_rev,partner_high6_rev,partner_high12_rev,partner_mixed2_rev,partner_mixed3_rev,partner_mixed6_rev,partner_mixed12_rev\n');

sublist = [102 109 110 113 115 117 118 119 120 121 122 123 124 125 126 127 128 131 132 135 136 137 138 139 140];

for s = 1:length(taskBFile)   
    subj_id = sublist(s);
    file_name = taskBFile(s).name;
    fname = fullfile(maindir,file_name);
    fid = fopen(fname);
    
    % defines what "C" (column) is from data output file
    C = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',');
    fclose(fid);
    
    trial_data = '';

    % define you_high means
    you_high2_means = [];
    you_high3_means = [];
    you_high6_means = [];
    you_high12_means = [];

    % define you_mixed means
    you_mixed2_means = [];
    you_mixed3_means = [];
    you_mixed6_means = [];
    you_mixed12_means = [];

    % define partner_high means
    partner_high2_means = [];
    partner_high3_means = [];
    partner_high6_means = [];
    partner_high12_means = [];

    % define partner_mixed means
    partner_mixed2_means = [];
    partner_mixed3_means = [];
    partner_mixed6_means = [];
    partner_mixed12_means = [];

    % define revs
    for i = 1:length(C{1})
        if isequal(C{8}(i),{'0'}) % non-computer responses
            if isequal(C{1}(i),{'1'}) % you_high
                if isequal(C{3}(i),{'2'}) % set size 2
                    you_high2 = str2double(C{6}(i));
                    you_high2_means = [you_high2_means,you_high2];
                elseif isequal(C{3}(i),{'3'}) % set size 3
                    you_high3 = str2double(C{6}(i));
                    you_high3_means = [you_high3_means,you_high3];
                elseif isequal(C{3}(i),{'6'}) % set size 6
                    you_high6 = str2double(C{6}(i));
                    you_high6_means = [you_high6_means,you_high6];
                elseif isequal(C{3}(i),{'12'}) % set size 12
                    you_high12 = str2double(C{6}(i));
                    you_high12_means = [you_high12_means,you_high12];
                end
            end
            if isequal(C{1}(i),{'2'}) % you_mixed
                if isequal(C{3}(i),{'2'}) % set size 2
                    you_mixed2 = str2double(C{6}(i));
                    you_mixed2_means = [you_mixed2_means,you_mixed2];
                elseif isequal(C{3}(i),{'3'}) % set size 3
                    you_mixed3 = str2double(C{6}(i));
                    you_mixed3_means = [you_mixed3_means,you_mixed3];
                elseif isequal(C{3}(i),{'6'}) % set size 6
                    you_mixed6 = str2double(C{6}(i));
                    you_mixed6_means = [you_mixed6_means,you_mixed6];
                elseif isequal(C{3}(i),{'12'}) % set size 12
                    you_mixed12 = str2double(C{6}(i));
                    you_mixed12_means = [you_mixed12_means,you_mixed12];
                end
            end
            if isequal(C{1}(i),{'5'}) % partner_high
                if isequal(C{3}(i),{'2'}) % set size 2
                    partner_high2 = str2double(C{6}(i));
                    partner_high2_means = [partner_high2_means,partner_high2];
                elseif isequal(C{3}(i),{'3'}) % set size 3
                    partner_high3 = str2double(C{6}(i));
                    partner_high3_means = [partner_high3_means,partner_high3];
                elseif isequal(C{3}(i),{'6'}) % set size 6
                    partner_high6 = str2double(C{6}(i));
                    partner_high6_means = [partner_high6_means,partner_high6];
                elseif isequal(C{3}(i),{'12'}) % set size 12
                    partner_high12 = str2double(C{6}(i));
                    partner_high12_means = [partner_high12_means,partner_high12];
                end
            end
            if isequal(C{1}(i),{'6'}) % partner_mixed
                if isequal(C{3}(i),{'2'}) % set size 2
                    partner_mixed2 = str2double(C{6}(i));
                    partner_mixed2_means = [partner_mixed2_means,partner_mixed2];
                elseif isequal(C{3}(i),{'3'}) % set size 3
                    partner_mixed3 = str2double(C{6}(i));
                    partner_mixed3_means = [partner_mixed3_means,partner_mixed3];
                elseif isequal(C{3}(i),{'6'}) % set size 6
                    partner_mixed6 = str2double(C{6}(i));
                    partner_mixed6_means = [partner_mixed6_means,partner_mixed6];
                elseif isequal(C{3}(i),{'12'}) % set size 12
                    partner_mixed12 = str2double(C{6}(i));
                    partner_mixed12_means = [partner_mixed12_means,partner_mixed12];
                end
            end
        end
    end

    % find you_high means
    you_high2_rev = mean(you_high2_means);
    you_high3_rev = mean(you_high3_means);
    you_high6_rev = mean(you_high6_means);
    you_high12_rev = mean(you_high12_means);

    % find you_mixed means
    you_mixed2_rev = mean(you_mixed2_means);
    you_mixed3_rev = mean(you_mixed3_means);
    you_mixed6_rev = mean(you_mixed6_means);
    you_mixed12_rev = mean(you_mixed12_means);

    % find partner_high means
    partner_high2_rev = mean(partner_high2_means);
    partner_high3_rev = mean(partner_high3_means);
    partner_high6_rev = mean(partner_high6_means);
    partner_high12_rev = mean(partner_high12_means);

    % find partner_mixed means
    partner_mixed2_rev = mean(partner_mixed2_means);
    partner_mixed3_rev = mean(partner_mixed3_means);
    partner_mixed6_rev = mean(partner_mixed6_means);
    partner_mixed12_rev = mean(partner_mixed12_means);

    % write in tmp_data
    tmp_data = [subj_id you_high2_rev you_high3_rev you_high6_rev you_high12_rev you_mixed2_rev you_mixed3_rev you_mixed6_rev you_mixed12_rev partner_high2_rev partner_high3_rev partner_high6_rev partner_high12_rev partner_mixed2_rev partner_mixed3_rev partner_mixed6_rev partner_mixed12_rev];

    % write data to output file 'setsize_revalRatings_zScores_output.csv'
    fprintf(fid_run,'%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n',tmp_data);
end
fclose(fid_run);
