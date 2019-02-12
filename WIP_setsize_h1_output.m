clear;
maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_h1_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id,Condition,2RT,3RT,6RT,12RT,monRT\n');

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
        for r = 1:length(C{12})
            x(r) = isequal(C{12}(r),{'0'});
        end
        
        % defines for later use
        r = length(find(x==1));
        Choice1RT = isequal(C{6}(r))
        
        % empty array to store data in
        tmp_data = zeros(r,4);
    
        % trial_data = beginning_part;
        
        % defines Condition
        if isequal(C{1}(r),{'1'});
            Condition == you_high;
        if isequal(C{1}(r),{'2'})
            Condition == you_mixed;
        if isequal(C{1}(r),{'5'})  
            Condition == partner_high;
        if isequal(C{1}(r),{'6'})
            Condition == partner_mixed;
            
        % creates empty array for data to be stored
        % you_high = zeros(1,r);
        % you_mixed = zeros(1,r);
        % partner_high = zeros(1,r);
        % partner_mixed = zeros(1,r);
        
        % defines RT's
        for you_high
            if isequal(C{5}(r),{'2'})
                2RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'3'})
                3RT == mean(Choice1RT);
            if isequal(C{5}(r),{'6'})
                6RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'12'})
                12RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'0.5'}) | isequal(C{5}(r),{'0.75'}) | isequal(C{5}(r),{'1.25'}) | isequal(C{5}(r),{'1.5'}) | isequal(C{5}(r),{'1.75'})
                monRT == mean(str2double(Choice1RT{:}));
            end
        for you_mixed
            if isequal(C{5}(r),{'2'})
                2RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'3'})
                3RT == mean(Choice1RT);
            if isequal(C{5}(r),{'6'})
                6RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'12'})
                12RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'0.5'}) | isequal(C{5}(r),{'0.75'}) | isequal(C{5}(r),{'1.25'}) | isequal(C{5}(r),{'1.5'}) | isequal(C{5}(r),{'1.75'})
                monRT == mean(str2double(Choice1RT{:}));
            end
        for partner_high
            if isequal(C{5}(r),{'2'})
                2RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'3'})
                3RT == mean(Choice1RT);
            if isequal(C{5}(r),{'6'})
                6RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'12'})
                12RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'0.5'}) | isequal(C{5}(r),{'0.75'}) | isequal(C{5}(r),{'1.25'}) | isequal(C{5}(r),{'1.5'}) | isequal(C{5}(r),{'1.75'})
                monRT == mean(str2double(Choice1RT{:}));
            end
        for partner_mixed
            if isequal(C{5}(r),{'2'})
                2RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'3'})
                3RT == mean(Choice1RT);
            if isequal(C{5}(r),{'6'})
                6RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'12'})
                12RT == mean(str2double(Choice1RT{:}));
            if isequal(C{5}(r),{'0.5'}) | isequal(C{5}(r),{'0.75'}) | isequal(C{5}(r),{'1.25'}) | isequal(C{5}(r),{'1.5'}) | isequal(C{5}(r),{'1.75'})
                monRT == mean(str2double(Choice1RT{:}));
            end
        end
            
        % write data to output file 'setsize_h1_output.tsv'
        fprintf(fid_run,trial_data);
        fprintf(fid_run,'%s,%s,%s,%s,%s/t%s,%s,%s,%s/t%s,%s,%s,%s/t%s,%s,%s,%s/n',subj,mean(tmp_data));
end
fclose(fid_run);
