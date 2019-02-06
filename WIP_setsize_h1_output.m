clc
clear all;
maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_h1_output.tsv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id\tChoosingForYou\tChoice1\tHighValue\tRT1\n');

% participants ran with latest task code. 999 is our test code to make sure
% that everything works properly
sublist = [999];

beginning_part = '999\t';
fname = 'output/subject_999_partner_998_task_b_results.csv';
fid = fopen(fname,'r');
for s = 1:length(sublist)
    
    subj = sublist(s);
    
    % turns these values into 8-bit integers in the string
    % highValue = int8.empty(0,run);
    
    % only include non-computer responses
    for i=1:180
        x(i) = isequal(C{12}(i),{'0'});
    end
    
    % define run
    run = length(find(x==1))
    
    % creates empty array for data to be stored
    you_high_RT = zeros(1,run);
    partner_high_RT = zeros(1,run);
    you_mixed_RT = zeros(1,run);
    partner_mixed_RT = zeros(1,run);

    % more empty arrays for data to be stored
    choosing_for_vals = zeros(1,run);
    tmp_data = zeros(run,1);
    
    % run each line of each participant's output file through this code
    for r=find(x==1)
        trial_data = beginning_part;
        % fname = fullfile(maindir,'psychopy','logs',num2str(subj),sprintf('sub-%03_partner_%03_task_b_results.csv',subj,r-1)); %creates variable to st|e the path to a given subject's data
        C = textscan(fopen(fname,'r'),'%s%s%s%s%s%s%s%s%s%s%s%s%s','Delimiter',',','HeaderLines',1);
        fclose(fid);
        
        % ChoosingForYou    
        if isequal(C{13}(r),{'1'})
            choosing_for_vals(r) = 1;
        else
            choosing_for_vals(r) = 0;
        end
       
        % Choice1
        choice = (C{5}(r));
        choice1(r) = choice{:};
        choice1 = string(C{5});
                    
        % HighValue
        if isequal(C{1}(r),{'1'}) | isequal(C{1}(r),{'3'}) | isequal(C{1}(r),{'5'}) | isequal(C{1}(r),{'7'})
            highValue(r) = 1;
            if choosing_for_vals(r) == 1 % choosing for yourself
                rt = C{6}(r);
                you_high_RT(r) = str2double(rt{:});
            else % choosing for your partner
                rt = C{6}(r);
                partner_high_RT(r) = str2double(rt{:});
            end
        else % is mixed value
            highValue(r) = 0; 
            if choosing_for_vals(r) == 1 % choosing for yourself
                rt = C{6}(r);
                you_mixed_RT(r) = str2double(rt{:});
            else % choosing for your partner
                rt = C{6}(r);
                partner_mixed_RT(r) = str2double(rt{:});
            end
        end
        
        % write data to output file 'setsize_h1_output.tsv'
        fprintf(fid_run,trial_data);
    end
    
end
fclose(fid_run);

