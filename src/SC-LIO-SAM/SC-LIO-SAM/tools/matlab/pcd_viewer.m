% Directory of .pcd scan files
pcd_dir = "/home/stapler/Desktop/Scans"; 

% Gets all scan file names 
pcd_names = listdir(pcd_dir);
list_out = pcd_names;

% Allocate memory to store pcd indixes
pcd_names_idx = 1:length(pcd_names);

% Iterate over all scan files
for ii = 1:length(pcd_names)
    % Extracts the file index by clipping the '.pcd' file ending 
    pcd_idx = str2double(pcd_names{ii}(1:end-4));
    % Adds the new pcd index
    pcd_names_idx(ii) = pcd_idx;
end

% Sort in ascending order
[test, sorted_loc] = sort(pcd_names_idx);
pcd_names_sorted = pcd_names(sorted_loc);


% Visualize through pointcloud show 
for ii = 1:length(pcd_names)

    figure(1);clf;
    pc = pcread(fullfile('/home','stapler','Desktop','Scans', pcd_names_sorted{ii}));
    pcshow(pc);

    % Test from matlab
    x = pc.Location(:,1);
    y = pc.Location(:,2);
    z = pc.Location(:,3);
    u = normals(:,1);
    v = normals(:,2);
    w = normals(:,3);
    hold on
    quiver3(x,y,z);
    hold off

    title(pcd_names_sorted{ii});

    %caxis([0, 200]);
    clim([0, 200]);
    
    xlim([-80, 80]);
    ylim([-80, 80]);
    zlim([-2, 15]);

end

