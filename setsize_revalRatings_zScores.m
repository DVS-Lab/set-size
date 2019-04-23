clear;
maindir = pwd;

% Get task B data
taskBFile = dir(fullfile(output_folder_path,...
        ['subject_' num2str(subj_id) '_partner*_task_b_results_z_scores_tt.csv']));

% Open Participant's task B data file
fname = taskBFile.name;
input_file = fopen(fname);
% Put data into cell struct
task_b_data = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',');

sublist = [102];

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
    you_high2RT_revs = [];
    you_high3RT_revs = [];
    you_high6RT_revs = [];
    you_high12RT_revs = [];
    you_highmonRT_revs = [];

    % define you_mixed means
    you_mixed2RT_revs = [];
    you_mixed3RT_revs = [];
    you_mixed6RT_revs = [];
    you_mixed12RT_revs = [];
    you_mixedmonRT_revs = [];

    % define partner_high means
    partner_high2RT_revs = [];
    partner_high3RT_revs = [];
    partner_high6RT_revs = [];
    partner_high12RT_revs = [];
    partner_highmonRT_means = [];

    % define partner_mixed means
    partner_mixed2RT_revs = [];
    partner_mixed3RT_revs = [];
    partner_mixed6RT_revs = [];
    partner_mixed12RT_revs = [];
    partner_mixedmonRT_revs = [];

    % define revs
    for i = 1:length(C{1})
        if isequal(C{8}(i),{'0'}) % non-computer responses
            if isequal(C{1}(i),{'1'}) % you_high
                if isequal(C{3}(i),{'2'}) % set size 2
                    you_high2RT = str2double(C{6}(i));
                    you_high2RT_means = [you_high2RT_means,you_high2RT];
                elseif isequal(C{3}(i),{'3'}) % set size 3
                    you_high3RT = str2double(C{6}(i));
                    you_high3RT_means = [you_high3RT_means,you_high3RT];
                elseif isequal(C{3}(i),{'6'}) % set size 6
                    you_high6RT = str2double(C{6}(i));
                    you_high6RT_means = [you_high6RT_means,you_high6RT];
                elseif isequal(C{3}(i),{'12'}) % set size 12
                    you_high12RT = str2double(C{6}(i));
                    you_high12RT_means = [you_high12RT_means,you_high12RT];
                else % monetary values
                    you_highmonRT = str2double(C{6}(i));
                    you_highmonRT_means = [you_highmonRT_means,you_highmonRT];
                end
            end
            if isequal(C{1}(i),{'2'}) % you_mixed
                if isequal(C{3}(i),{'2'}) % set size 2
                    you_mixed2RT = str2double(C{6}(i));
                    you_mixed2RT_means = [you_mixed2RT_means,you_mixed2RT];
                elseif isequal(C{3}(i),{'3'}) % set size 3
                    you_mixed3RT = str2double(C{6}(i));
                    you_mixed3RT_means = [you_mixed3RT_means,you_mixed3RT];
                elseif isequal(C{3}(i),{'6'}) % set size 6
                    you_mixed6RT = str2double(C{3}(i));
                    you_mixed6RT_means = [you_mixed6RT_means,you_mixed6RT];
                elseif isequal(C{3}(i),{'12'}) % set size 12
                    you_mixed12RT = str2double(C{6}(i));
                    you_mixed12RT_means = [you_mixed12RT_means,you_mixed12RT];
                else % monetary values
                    you_mixedmonRT = str2double(C{6}(i));
                    you_mixedmonRT_means = [you_mixedmonRT_means,you_mixedmonRT];
                end
            end
            if isequal(C{1}(i),{'5'}) % partner_high
                if isequal(C{3}(i),{'2'}) % set size 2
                    partner_high2RT = str2double(C{6}(i));
                    partner_high2RT_means = [partner_high2RT_means,partner_high2RT];
                elseif isequal(C{3}(i),{'3'}) % set size 3
                    partner_high3RT = str2double(C{6}(i));
                    partner_high3RT_means = [partner_high3RT_means,partner_high3RT];
                elseif isequal(C{3}(i),{'6'}) % set size 6
                    partner_high6RT = str2double(C{6}(i));
                    partner_high6RT_means = [partner_high6RT_means,partner_high6RT];
                elseif isequal(C{3}(i),{'12'}) % set size 12
                    partner_high12RT = str2double(C{6}(i));
                    partner_high12RT_means = [partner_high12RT_means,partner_high12RT];
                else % monetary values
                    partner_highmonRT = str2double(C{6}(i));
                    partner_highmonRT_means = [partner_highmonRT_means,partner_highmonRT];
                end
            end
            if isequal(C{1}(i),{'6'}) % partner_mixed
                if isequal(C{3}(i),{'2'}) % set size 2
                    partner_mixed2RT = str2double(C{6}(i));
                    partner_mixed2RT_means = [partner_mixed2RT_means,partner_mixed2RT];
                elseif isequal(C{3}(i),{'3'}) % set size 3
                    partner_mixed3RT = str2double(C{6}(i));
                    partner_mixed3RT_means = [partner_mixed3RT_means,partner_mixed3RT];
                elseif isequal(C{3}(i),{'6'}) % set size 6
                    partner_mixed6RT = str2double(C{6}(i));
                    partner_mixed6RT_means = [partner_mixed6RT_means,partner_mixed6RT];
                elseif isequal(C{3}(i),{'12'}) % set size 12
                    partner_mixed12RT = str2double(C{6}(i));
                    partner_mixed12RT_means = [partner_mixed12RT_means,partner_mixed12RT];
                else % monetary values
                    partner_mixedmonRT = str2double(C{6}(i));
                    partner_mixedmonRT_means = [partner_mixedmonRT_means,partner_mixedmonRT];
                end
            end
        end
    end

    % find you_high means
    you_high2RT_rev = mean(you_high2RT_revs);
    you_high3RT_rev = mean(you_high3RT_revs);
    you_high6RT_rev = mean(you_high6RT_revs);
    you_high12RT_rev = mean(you_high12RT_revs);
    you_highmonRT_rev = mean(you_highmonRT_revs);

    % find you_mixed means
    you_mixed2RT_rev = mean(you_mixed2RT_revs);
    you_mixed3RT_rev = mean(you_mixed3RT_revs);
    you_mixed6RT_rev = mean(you_mixed6RT_revs);
    you_mixed12RT_rev = mean(you_mixed12RT_revs);
    you_mixedmonRT_rev = mean(you_mixedmonRT_revs);

    % find partner_high means
    partner_high2RT_rev = mean(partner_high2RT_revs);
    partner_high3RT_rev = mean(partner_high3RT_revs);
    partner_high6RT_rev = mean(partner_high6RT_revs);
    partner_high12RT_rev = mean(partner_high12RT_revs);
    partner_highmonRT_rev = mean(partner_highmonRT_revs);

    % find partner_mixed means
    partner_mixed2RT_rev = mean(partner_mixed2RT_revs);
    partner_mixed3RT_rev = mean(partner_mixed3RT_revs);
    partner_mixed6RT_rev = mean(partner_mixed6RT_revs);
    partner_mixed12RT_rev = mean(partner_mixed12RT_revs);
    partner_mixedmonRT_rev = mean(partner_mixedmonRT_revs);

    % write in tmp_data
    tmp_data = [subj_id you_high2RT_rev you_high3RT_rev you_high6RT_rev you_high12RT_rev you_highmonRT_rev you_mixed2RT_rev you_mixed3RT_rev you_mixed6RT_rev you_mixed12RT_rev you_mixedmonRT_rev partner_high2RT_rev partner_high3RT_rev partner_high6RT_rev partner_high12RT_rev partner_highmonRT_rev partner_mixed2RT_rev partner_mixed3RT_rev partner_mixed6RT_rev partner_mixed12RT_rev partner_mixedmonRT_rev];

    % write data to output file 'setsize_revalRatings_zScores_output.csv'
    fprintf(fid_run,'%d,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n',tmp_data);
end
fclose(fid_run);
