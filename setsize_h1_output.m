clear;
maindir = pwd;

% open output files
fname = fullfile(maindir,'setsize_h1_output.csv');
fid_run = fopen(fname,'w'); % csv uses commans (,) & tsv uses tabs (\t)
fprintf(fid_run,'subject_id,you_high2RT,you_high3RT,you_high6RT,you_high12RT,you_highmonRT,you_mixed2RT,you_mixed3RT,you_mixed6RT,you_mixed12RT,you_mixedmonRT,partner_high2RT,partner_high3RT,partner_high6RT,partner_high12RT,partner_highmonRT,partner_mixed2RT,partner_mixed3RT,partner_mixed6RT,partner_mixed12RT,partner_mixedmonRT\n');

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
        Choice1RT = C{6};
        % Choice1RT = zeros(1,r);
        
        % empty array to store data in
        tmp_data = zeros(s,21);
        % tmp_data = zeros(# of subjects,21 rows in the analysis output file)
    
        trial_data = beginning_part;
        
        % defines RT's
        if isequal(C{1}(:),{'1'}) % you_high
            if isequal(C{5}(:),{'2'})
                you_high2RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'3'})
                you_high3RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'6'})
                you_high6RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'12'})
                you_high12RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'0.5'}) || isequal(C{5}(:),{'0.75'}) || isequal(C{5}(:),{'1.25'}) || isequal(C{5}(:),{'1.5'}) || isequal(C{5}(:),{'1.75'})
                you_highmonRT = mean(str2double(Choice1RT{:}));
            end
        end
        if isequal(C{1}(:),{'2'}) % you_mixed
            if isequal(C{5}(:),{'2'})
                you_mixed2RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'3'})
                you_mixed3RT = mean(Choice1RT);
            elseif isequal(C{5}(:),{'6'})
                you_mixed6RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'12'})
                you_mixed12RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'0.5'}) || isequal(C{5}(:),{'0.75'}) || isequal(C{5}(:),{'1.25'}) || isequal(C{5}(:),{'1.5'}) || isequal(C{5}(:),{'1.75'})
                you_mixedmonRT = mean(str2double(Choice1RT{:}));
            end
        end
        if isequal(C{1}(:),{'5'}) % partner_high
            if isequal(C{5}(:),{'2'})
                partner_high2RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'3'})
                partner_high3RT = mean(Choice1RT);
            elseif isequal(C{5}(:),{'6'})
                partner_high6RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'12'})
                partner_high12RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'0.5'}) || isequal(C{5}(r),{'0.75'}) || isequal(C{5}(:),{'1.25'}) || isequal(C{5}(:),{'1.5'}) || isequal(C{5}(:),{'1.75'})
                partner_highmonRT = mean(str2double(Choice1RT{:}));
            end
        end
        if isequal(C{1}(:),{'6'}) % partner_mixed
            if isequal(C{5}(:),{'2'})
                partner_mixed2RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'3'})
                partner_mixed3RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'6'})
                partner_mixed6RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'12'})
                partner_mixed12RT = mean(str2double(Choice1RT{:}));
            elseif isequal(C{5}(:),{'0.5'}) || isequal(C{5}(:),{'0.75'}) || isequal(C{5}(:),{'1.25'}) || isequal(C{5}(:),{'1.5'}) || isequal(C{5}(:),{'1.75'})
                partner_mixedmonRT = mean(str2double(Choice1RT{:}));
            end
        end
        
        % write in tmp_data
        tmp_data(r,:) = [you_high2RT you_high3RT you_high6RT you_high12RT you_highmonRT you_mixed2RT you_mixed3RT you_mixed6RT you_mixed12RT you_mixedmonRT partner_high2RT partner_high3RT partner_high6RT partner_high12RT partner_highmonRT partner_mixed2RT partner_mixed3RT partner_mixed6RT partner_mixed12RT partner_mixedmonRT];
        
        % write data to output file 'setsize_h1_output.tsv'
        fprintf(fid_run,'%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s/n',subj,tmp_data);
end
fclose(fid_run);
