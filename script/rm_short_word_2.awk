{
    if( length($1) <= 2 ){ # remove short word
        next;
    }
    print $0;
}
