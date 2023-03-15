% Directory of .pcd scan files
pcd_dir = "/home/stapler1/Desktop"; 



    figure(1);clf;
    pc = pcread(fullfile(pcd_dir,'cloudGlobal.pcd'));
    pcshow(pc);

    %caxis([0, 200]);
    clim([0, 200]);
    
    xlim([-80, 80]);
    ylim([-80, 80]);
    zlim([-2, 15]);


