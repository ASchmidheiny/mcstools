import numpy as np


def spherical_coords_mcenter(radius: float, colat: float, lat: float) -> np.array:
    """
    Return vector in spherical coordinates given r, theta, phi
    """
    return np.array([radius, colat, lat])


def spherical_to_cartesian(spher_vec: np.array) -> np.array:
    """
    Convert vector in spherical coordinates to cartesian x, y, z.
    """
    r = spher_vec[0]
    colat = spher_vec[1]
    lon = spher_vec[2]
    return np.array(
        [
            r * np.cos(lon) * np.sin(colat),
            r * np.sin(lon) * np.sin(colat),
            r * np.cos(colat),
        ]
    )


def mcs_view_angle_to_sc_body_frame(elevation_angle, azimuth_angle):
    """
    Convert mcs view to spacecraft body frame given elevation
    and azimuth angle.
    Angles given in degrees.
    """
    r = 1
    theta = (180 - elevation_angle) * np.pi / 180
    phi = (azimuth_angle - 180) * np.pi / 180
    return spherical_to_cartesian(np.array([r, theta, phi]))


def scattering_angle(solar_incidence_vector, view_vector):
    """
    Compute the scattering angle given a solar incidence vector
    and view vector. Really just computing the two vectors
    and subtracting from pi.
    0 = forward scattering
    180 = back scattering
    """
    return np.rad2deg(
        np.pi
        - np.arccos(
            (np.dot(solar_incidence_vector, view_vector))
            / np.dot(
                np.linalg.norm(solar_incidence_vector), np.linalg.norm(view_vector)
            )
        )
    )
