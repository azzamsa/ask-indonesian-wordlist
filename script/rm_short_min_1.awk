{
    if( length($1) <= 1 ){ # remove short word
        next;
    }
    print $0;
}
