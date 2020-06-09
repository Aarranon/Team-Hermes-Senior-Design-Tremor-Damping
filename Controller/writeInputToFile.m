function writeInputToFile(input)
   fid = fopen( 'Output/inputTimeSeries.csv', 'a' );
    for jj = 1 : length( input )
        fprintf( fid, '%d\n', input(jj) );
    end
    fclose( fid );