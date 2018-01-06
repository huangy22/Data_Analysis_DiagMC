
  !============== Variable Module ====================================
  MODULE my_vrbls
    IMPLICIT NONE

    double precision, parameter :: eps    = 1.d-14            ! very small number
    double precision, parameter :: tol    = 0.15d0            ! tolerance for Cor

    integer :: Lx
    double precision :: Beta
    integer :: NBlck=5120
    integer :: MXNCPU = 500
    integer :: iblck,TotSamp,Seed
    double precision :: JJ,Q, J3, h

    !character(8 ), parameter :: ident = 'hs_sqa 0'            ! identifier
    character(8 )  :: ident             ! identifier
    character(50)  :: infile         ! datafile
    character(50)  :: outfile         ! datafile
    character(50)  :: filename
    !-----------------------------------------------------------------

    !-- Observables --------------------------------------------------
    !! THIS IS PROJECT-DEPENDENT 
    integer, parameter :: NObs_b = 17                         ! #basic observables
    integer, parameter :: NObs_c = 5                          ! #composite observables
    integer, parameter :: NObs   = NObs_b+NObs_c              ! Total # observables
    character(30), dimension(NObs) :: QuanName       
    !-----------------------------------------------------------------

    !-- Statistics ---------------------------------------------------
    ! THIS IS PROJECT-INDEPENDENT 
    double precision, allocatable :: Quan(:,:), Err(:,:)       ! 1st--#quan.  2nd--#block
    double precision, allocatable :: Ave(:), Dev(:), Cor(:)           ! average, error bars, and correlation of observables
    !-----------------------------------------------------------------

    
  END MODULE my_vrbls

  !=====Main routine for bond percolation on square lattice ==========
  PROGRAM main
    use my_vrbls
    implicit none
    integer :: whichone,stat,Samp,ind
    integer :: i,j,flag

    call property_name

    allocate(Quan(1:NObs, 1:MXNCPU), Err(1:NObs, 1:MXNCPU))
    allocate(Ave(1:NObs), Dev(1:NObs), Cor(1:NObs))

    call get_command_argument(1, filename)
    infile = "./OriginalData/"//Trim(filename)//"_hs_sqa0.dat"
    outfile = Trim(filename)//"_ext_hs_sqa0.txt"
    print *, infile, outfile

    open(8,file=infile) 
    ind=0
    flag=1
    TotSamp = 0
    do while(ind<=MXNCPU)
        read(8, *,iostat=stat);
        if(stat/=0) exit

        ind=ind+1
	read(8, 40) ident, Lx, beta, JJ, J3, Q, Seed, Samp
	40 format(a8,i6,4f12.6,i12,i8)
	TotSamp = TotSamp + Samp

	do j = 1, Nobs
	  read(8,41) i, Quan(j,ind), Err(j,ind), Cor(j)
	  41 format(i4,2f25.15,f12.5)
	enddo
	do j = 1, 5
	  read(8,*) 
      enddo
    enddo
    close(8)

    if(ind>=1) then
        call stat_alan(ind)
        call write2file()
    endif

  CONTAINS

  SUBROUTINE property_name
    implicit none
    QuanName( 1)= "Potential" !! Beta*potential energy
    QuanName( 2)= "Kinetic"   !! Beta*kinetic energy
    QuanName( 3)= "Energy"    !! Beta*Energy/Vol
    QuanName( 4)= "Energy^2"  !! Energy^2/Vol^2
    QuanName( 5)= "Wx"        !! Winding on x
    QuanName( 6)= "Wy"        !! Winding on y
    QuanName( 7)= "Wz"        !! Winding on z
    QuanName( 8)= "Stiffness" !! stiffness
    QuanName( 9)= "Magnet^2 density"  !! winding on tau==Magnetization
    QuanName(10)= "Magnet^4 density"  !! M^4
    QuanName(11)= "UnifChi"   !! Spatial Susceptibility 
    QuanName(12)= "StagMag"   !! Staggerd Magnetization 
    QuanName(13)= "StagMagnet^2 density"  !! Staggerd Magnetization 
    QuanName(14)= "StagMagnet^4 density"  !! staggered M^4
    QuanName(15)= "StagChi"       !! Spatial Susceptibility 
    QuanName(16)= "W0"
    QuanName(17)= "W1"
    QuanName(18)= "WL/Wt"
    QuanName(19)= "W0/W1"
    QuanName(20)= "UnifQ"
    QuanName(21)= "StagQ"
    QuanName(22)= "SpecificHeat"
  END SUBROUTINE

  SUBROUTINE stat_alan(nfile)
    implicit none
    integer          :: i, j, k, k0, nfile
    logical          :: prt
    double precision :: devn, devp, nor
    double precision, allocatable :: Aux(:)

    nor  = 1.d0/(nfile*1.d0)

    ! -- calculate average -------------------------------------------
    do j = 1, NObs
      Ave(j) = nor*Sum(Quan(j,1:nfile))
    enddo

    DO j = 1, NObs
      Dev(j) = 0.d0
      do k = 1,  nfile
        devn   = Quan(j,k)-Ave(j)
        Dev(j) = Dev(j)+devn*devn
      enddo 
      Dev(j)   = Dev(j)*nor
      Dev(j)   = dsqrt(Dev(j)/(nfile-1.d0))
    ENDDO 

    return
  END SUBROUTINE stat_alan

  SUBROUTINE write2file 
    implicit none
    integer       :: i, j, k, Nwri

    open (8,file=outfile) 

    write(8, *) "{"
    do j = 1, Nobs-1
      write(8,*) "'", Trim(QuanName(j)), "': {'error': ", Dev(j), ", 'value': ", Ave(j), "},"
    enddo
    write(8,*) "'", Trim(QuanName(NObs)), "': {'error': ", Dev(NObs), ", 'value': ", Ave(NObs), "}}"
    close(8)
    return
  END SUBROUTINE write2file

END PROGRAM main
!=====================================================================
