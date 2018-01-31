{
    if( $1 ~ /.com$|.id$|.org$/){ # remove date
        next;
    }
    print $0;
}
