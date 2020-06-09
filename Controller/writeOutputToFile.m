function writeOutputToFile(input)
    fid = fopen( 'Output/outputTimeSeries.csv', 'a' );
    for jj = 1 : length( input )
        fprintf( fid, '%d\n', input(jj) );
    end
    fclose( fid );