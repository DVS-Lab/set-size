clc
clear;
maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_h1_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id,ChoosingForYou,Choice1,highValue,RT1\n');

% fake subject_ID (999 is to practice with)
sublist = (999);

for s = 1:length(sublist)
    
    subj = sublist(s);
   
    beginning_part = '999\t';
    fname = fullfile(maindir,'output/subject_999_partner_998_task_b_results.csv');
    fid = fopen(fname,'r');
    % defines what "C" (column) is from data output file
    C = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
    fclose(fid);
        
        % only include non-computer responses
        for i=1:180
            x(i) = isequal(C{12}(i),{'0'});
        end
        
        % define runs
        runs = find(x==1);
    
        trial_data = beginning_part;
        
        % turns these values into 8-bit integers in the string
        % highValue = int8.empty(0,run);

        % define r
        r = length(find(x==1))
        
        % empty array to store data in
        tmp_data = zeros(r,1);

        % creates empty array for data to be stored
        you_high_RT = zeros(1,r);
        partner_high_RT = zeros(1,r);
        you_mixed_RT = zeros(1,r);
        partner_mixed_RT = zeros(1,r);

        % more empty arrays for data to be stored
        choosing_for_vals = zeros(1,r);

        % ChoosingForYou    
        if isequal(C{13}(r),{'1'})
            choosing_for_vals(r) = 1;
        else
            choosing_for_vals(r) = 0;
        end

        % defines Choice1
        choice1(r) = (C{5}(r));
        choice1 = string(C{5});

        % defines Value
        if isequal(C{1}(r),{'1'}) | isequal(C{1}(r),{'3'}) | isequal(C{1}(r),{'5'}) | isequal(C{1}(r),{'7'})
            highValue(r) = 1;
            if choosing_for_vals(r) == 1 % choosing for yourself
                rt = C{6}(r);
                you_high_RT(r) = mean(str2double(rt{:}));
            else % choosing for your partner
                rt = C{6}(r);
                partner_high_RT(r) = mean(str2double(rt{:}));
            end
        else % is mixed value
            highValue(r) = 0; 
            if choosing_for_vals(r) == 1 % choosing for yourself
                rt = C{6}(r);
                you_mixed_RT(r) = mean(str2double(rt{:}));
            else % choosing for your partner
                rt = C{6}(r);
                partner_mixed_RT(r) = mean(str2double(rt{:}));
            end
        end

        % write data to output file 'setsize_h1_output.tsv'
        fprintf(fid_run,trial_data);
        fprintf('setsize_h1_output.tsv');
end
fprintf(fid_run,'%s,%s,%s,%s,%s/t%s,%s,%s,%s/t%s,%s,%s,%s/t%s,%s,%s,%s/n',subj,mean(tmp_data));
fclose(fid_run);
